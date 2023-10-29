import { Injectable } from '@nestjs/common';
import { PrismaService } from 'src/prisma/prisma.service';

@Injectable()
export class ShopService {
  constructor(private prismaService: PrismaService) {}

  async getItems(): Promise<{ [k: string]: any }[]> {
    const items = await this.prismaService.shop.findMany({
      select: {
        id: true,
        name: true,
        price: true,
        image: true,
      },
    });
    return items;
  }

  async buyItem(id: number, userId: number): Promise<void> {
    const user = await this.prismaService.user.findUnique({
      where: {
        id: userId,
      },
    });
    const item = await this.prismaService.shop.findUnique({
      where: {
        id: id,
      },
    });
    if (user.balance < item.price) {
      throw new Error('Not enough money');
    }

    await this.prismaService.user.update({
      where: {
        id: userId,
      },
      data: {
        balance: user.balance - item.price,
      },
    });

    await this.prismaService.user.update({
      where: {
        id: userId,
      },
      data: {
        purchasedItems: [...user.purchasedItems, item.name],
      },
    });
  }

  async getItemContent(itemId: number): Promise<{ [k: string]: any }> {
    const item = await this.prismaService.shop.findUnique({
      where: {
        id: itemId,
      },
    });
    return item;
  }

  async addBalance(userId: number, amount: number): Promise<void> {
    const user = await this.prismaService.user.findUnique({
      where: {
        id: userId,
      },
    });

    await this.prismaService.user.update({
      where: {
        id: userId,
      },
      data: {
        balance: user.balance + amount,
      },
    });
  }

  async getItemByName(name: string): Promise<{ [k: string]: any }> {
    const item = await this.prismaService.shop.findUnique({
      where: {
        name: name,
      },
    });
    return item;
  }
}
