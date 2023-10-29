import { Injectable } from '@nestjs/common';
import { PrismaService } from 'src/prisma/prisma.service';

function exclude<User, Key extends keyof User>(user: User, keys: any[]) {
  return Object.fromEntries(
    Object.entries(user).filter(([key]) => !keys.includes(key)),
  );
}

@Injectable()
export class UserService {
  constructor(private prismaService: PrismaService) {}

  async getUser(id: number): Promise<{ [k: string]: any }> {
    const user = await this.prismaService.user.findUnique({
      where: {
        id: id,
      },
    });
    const ret = exclude(user, ['password', 'createdAt', 'updatedAt', 'role']);
    return ret;
  }
}
