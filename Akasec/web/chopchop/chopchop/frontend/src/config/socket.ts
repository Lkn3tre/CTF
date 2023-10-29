import io from "socket.io-client";
import { Cookies } from "react-cookie";

export const socket = io("/api", {
  extraHeaders: {
    Authorization: `Bearer ${new Cookies().get("token")}`,
  },
  autoConnect: false,
});
