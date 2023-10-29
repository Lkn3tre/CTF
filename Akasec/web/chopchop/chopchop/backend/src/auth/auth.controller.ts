import { Body, Controller, HttpStatus, Post, Res } from '@nestjs/common';
import { AuthService } from './auth.service';
import { LoginDto, RegisterDto } from 'src/dto/auth.dto';

@Controller('auth')
export class AuthController {
  constructor(private authService: AuthService) {}

  @Post('register')
  async register(@Body() data: RegisterDto, @Res() res): Promise<void> {
    try {
      await this.authService.register(data);
      res.status(HttpStatus.OK).send('User registered');
    } catch (error) {
      res.status(HttpStatus.BAD_REQUEST).send(error.message);
    }
  }

  @Post('login')
  async login(@Body() data: LoginDto, @Res() res): Promise<void> {
    try {
      const ret = await this.authService.login(data.email, data.password);
      res.status(HttpStatus.OK).send(ret);
    } catch (error) {
      res.status(HttpStatus.UNAUTHORIZED).send(error.message);
    }
  }
}
