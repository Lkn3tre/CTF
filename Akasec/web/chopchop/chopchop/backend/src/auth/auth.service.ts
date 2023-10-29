import { Injectable } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import { RegisterDto } from 'src/dto/auth.dto';
import { PrismaService } from 'src/prisma/prisma.service';
import { compare, hash } from 'bcrypt';
import { jwt_conf } from 'src/config/jwt';

@Injectable()
export class AuthService {
  constructor(
    private jwtService: JwtService,
    private prismaService: PrismaService,
  ) {}

  async register(data: RegisterDto) {
    const { name, email, password } = data;
    const user = await this.prismaService.user.findFirst({
      where: {
        email: email,
      },
    });
    if (user) {
      throw new Error('User already exists');
    }
    const hpass = await hash(password, 10);
    const newUser = await this.prismaService.user.create({
      data: {
        username: name,
        email: email,
        password: hpass,
      },
    });
    return {
      status: 200,
      message: 'User created successfully',
    };
  }

  async login(email: string, password: string) {
    const user = await this.prismaService.user.findFirst({
      where: {
        email: email,
      },
    });
    if (!user) {
      throw new Error('Invalid Username or Password');
    }
    const valid = await compare(password, user.password);
    if (!valid) {
      throw new Error('Invalid Username or Password');
    }
    const token = this.jwtService.sign(
      {
        id: user.id,
        email: user.email,
        role: 'recruit',
      },
      {
        secret: jwt_conf.secret,
        expiresIn: 3600,
      },
    );
    return {
      token: token,
    };
  }
}
