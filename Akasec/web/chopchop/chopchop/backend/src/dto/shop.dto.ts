import { IsNotEmpty, IsNumber } from 'class-validator';

export class CheckoutDTO {
  @IsNotEmpty()
  @IsNumber()
  id: number;
}
