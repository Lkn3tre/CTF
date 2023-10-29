import { IsNotEmpty, IsNumber, IsString, Length } from 'class-validator';

export class RedeemDTO {
  @IsNotEmpty()
  @IsString()
  @Length(1, 100)
  voucher: string;
}
