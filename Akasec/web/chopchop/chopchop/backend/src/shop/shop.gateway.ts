import {
  SubscribeMessage,
  WebSocketGateway,
  WebSocketServer,
} from '@nestjs/websockets';
import {
  OnGatewayInit,
  OnGatewayConnection,
  OnGatewayDisconnect,
} from '@nestjs/websockets';
import { JwtService } from '@nestjs/jwt';
import { UseGuards } from '@nestjs/common';
import { WsGuard } from './ws/ws.guard';
import { Server } from 'socket.io';
import { jwt_conf } from 'src/config/jwt';

// TODO: make this gateway usable and migrate the voucher to nestjs.
@WebSocketGateway()
@UseGuards(WsGuard)
export class ShopGateway implements OnGatewayConnection, OnGatewayDisconnect {
  constructor(private jwtService: JwtService) {}

  @WebSocketServer() server: Server;
  clients = new Map<string, any>();

  @UseGuards(WsGuard)
  async handleConnection(client: any, ...args: any[]): Promise<void> {
    try {
      const authHeader = client.handshake.headers.authorization;
      if (authHeader === undefined || authHeader === null)
        throw new Error('Not authorized');
      const token = authHeader.split(' ')[1];
      const user = await this.jwtService.verifyAsync(token, {
        secret: jwt_conf.secret,
      });
      client.user = user;
      this.clients.set(user.id, client);
    } catch (e) {
      client.disconnect();
    }
  }

  async handleDisconnect(client: any): Promise<void> {
    // console.log('ShopGateway Disconnect');
  }

  @SubscribeMessage('msgToSupport')
  @UseGuards(WsGuard)
  async handleMessage(client: any, payload: any): Promise<void> {
    this.server
      .to(client.id)
      .emit('msgToClient', 'Hello there ! Support is unavaible right now.');
  }
}
