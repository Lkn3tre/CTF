import React from "react";
import { instance } from "../../config/config";
import { useCookies } from "react-cookie";
import {
  Input,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  Button,
  useToast,
} from "@chakra-ui/react";

interface Props {
  onClose: () => void;
  isOpen: boolean;
}

export default function Redeem({ onClose, isOpen }: Props) {
  const [voucher, setVoucher] = React.useState<string>();
  const [cookies] = useCookies(["token"]);
  const toast = useToast();
  const handleRedeem = () => {
    instance
      .post(
        "/shop/redeem",
        {
          voucher: voucher,
        },
        {
          headers: {
            Authorization: `Bearer ${cookies.token}`,
          },
        },
      )
      .then(() => {
        window.location.href = "/items";
      })
      .catch((err) => {
        console.log(err);
        toast({
          title: "Error",
          description: "Invalid voucher code",
          status: "error",
          duration: 5000,
          isClosable: true,
        });
      });
  };

  return (
    <Modal isOpen={isOpen} onClose={onClose}>
      <ModalOverlay />
      <ModalContent>
        <ModalHeader>Redeem a voucher</ModalHeader>
        <ModalCloseButton />
        <ModalBody>
          <Input
            placeholder="Voucher code"
            onChange={(e) => setVoucher(e.target.value)}
          />
        </ModalBody>

        <ModalFooter>
          <Button onClick={handleRedeem} colorScheme="whatsapp">
            Redeem
          </Button>
          <Button colorScheme="blue" mx={2} onClick={onClose}>
            Close
          </Button>
        </ModalFooter>
      </ModalContent>
    </Modal>
  );
}
