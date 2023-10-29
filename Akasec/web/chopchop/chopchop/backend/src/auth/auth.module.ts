import { Module } from '@nestjs/common';
import { AuthController } from './auth.controller';
import { AuthService } from './auth.service';
import { PrismaModule } from 'src/prisma/prisma.module';
import { PassportModule } from '@nestjs/passport';
import { JwtModule } from '@nestjs/jwt';
import { jwt_conf } from 'src/config/jwt';
import { JwtStrategy } from './jwt/jwt.strategy';
import { PrivJwtStrategy } from './jwt/jwt-priv.strategy';

@Module({
  imports: [
    PrismaModule,
    PassportModule.register({
      defaultStrategy: 'jwt',
      property: 'user',
      session: false,
    }),
    JwtModule.register({
      secret: jwt_conf.secret,
      signOptions: {
        expiresIn: jwt_conf.expired,
      },
    }),
  ],
  controllers: [AuthController],
  providers: [AuthService, JwtStrategy, PrivJwtStrategy],
})
export class AuthModule {}
