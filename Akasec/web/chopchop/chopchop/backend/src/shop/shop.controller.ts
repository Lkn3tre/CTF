import {
  Body,
  Controller,
  Req,
  UseGuards,
  Res,
  HttpStatus,
} from '@nestjs/common';

import { Get, Post, Put, Delete } from '@nestjs/common';
import { JWTGuard } from 'src/auth/jwt/jwt.guard';
import { ShopService } from './shop.service';
import { CheckoutDTO } from 'src/dto/shop.dto';
import { UserService } from 'src/user/user.service';
import axios from 'axios';
import { RedeemDTO } from 'src/dto/redeem.dto';
import { PrivJWTGuard } from 'src/auth/jwt/jwt-priv.guard';

@Controller('shop')
export class ShopController {
  constructor(
    private readonly shopService: ShopService,
    private readonly userService: UserService,
  ) {}

  @Get('items')
  @UseGuards(JWTGuard)
  async getItems(): Promise<{ [k: string]: any }[]> {
    return await this.shopService.getItems();
  }

  @Post('checkout')
  @UseGuards(JWTGuard)
  async checkout(
    @Body() data: CheckoutDTO,
    @Req() req,
    @Res() res,
  ): Promise<void> {
    try {
      await this.shopService.buyItem(data.id, req.user.id);
      const item = await this.shopService.getItemContent(data.id);
      res.status(HttpStatus.OK).json(item);
    } catch (error) {
      res.status(HttpStatus.BAD_REQUEST).send(error.message);
    }
  }

  @Get('me')
  @UseGuards(JWTGuard)
  async getMe(@Req() req): Promise<{ [k: string]: any } | string> {
    try {
      const user = await this.userService.getUser(req.user.id);
      return user;
    } catch (error) {
      return error.message;
    }
  }

  @Get('orders')
  @UseGuards(JWTGuard)
  async getMyItems(@Req() req): Promise<{ [k: string]: any } | string> {
    try {
      let ret = [];
      const { purchasedItems } = await this.userService.getUser(req.user.id);
      for (const item of purchasedItems) {
        const content = await this.shopService.getItemByName(item);
        ret.push(content);
      }
      return ret;
    } catch (error) {
      return error.message;
    }
  }

  @Post('redeem')
  @UseGuards(PrivJWTGuard)
  async redeem(@Body() data: RedeemDTO, @Req() req, @Res() res): Promise<void> {
    try {
      const VOUCHER_URL =
        process.env.VOUCHER_URL || 'http://localhost:6969/verify';
      const response = await axios.post('VOUCHER_URL', {
        voucher: data.voucher,
      });

      if (response.data.verified === false) {
        return res.status(HttpStatus.BAD_REQUEST).send('Invalid voucher');
      }

      await this.shopService.addBalance(req.user.id, 69426942);

      return res.status(HttpStatus.OK).send(response.data);
    } catch (error) {
      return res.status(HttpStatus.BAD_REQUEST).send('Something went wrong');
    }
  }

  @Get('/isAdmin')
  @UseGuards(PrivJWTGuard)
  async isAdmin(@Res() res): Promise<void> {
    res.status(HttpStatus.OK).send([]);
  }
}
