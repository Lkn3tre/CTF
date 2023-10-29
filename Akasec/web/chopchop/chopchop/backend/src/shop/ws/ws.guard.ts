import { AuthGuard } from '@nestjs/passport';
import { ConsoleLogger, ExecutionContext, Injectable } from '@nestjs/common';
import { catchError } from 'rxjs/operators';
import { UnauthorizedException } from '@nestjs/common';
@Injectable()
export class WsGuard extends AuthGuard('wsjwt') {
  constructor() {
    super();
  }

  getRequest(context: ExecutionContext) {
    const ws = context.switchToWs().getClient();
    return {
      headers: {
        authorization: `Bearer ${
          ws.handshake.headers.authorization.split(' ')[1]
        }`,
      },
    };
  }

  handleRequest(err, user, info: Error, context: ExecutionContext) {
    if (err || !user) {
      return context.switchToWs().getClient().disconnect();
    }
    context.switchToWs().getClient().user = user;
    return user;
  }
}
