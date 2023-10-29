import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { PrismaModule } from './prisma/prisma.module';
import { AuthModule } from './auth/auth.module';
import { ShopController } from './shop/shop.controller';
import { ShopGateway } from './shop/shop.gateway';
import { JwtService } from '@nestjs/jwt';
import { Wsjwt } from './shop/ws/ws.strategy';
import { ShopService } from './shop/shop.service';
import { UserService } from './user/user.service';

@Module({
  imports: [PrismaModule, AuthModule],
  controllers: [AppController, ShopController],
  providers: [
    AppService,
    ShopGateway,
    JwtService,
    Wsjwt,
    ShopService,
    UserService,
  ],
})
export class AppModule {}
