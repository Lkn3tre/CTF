import React from "react";
import {
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  Flex,
  Input,
  Icon,
  IconButton,
  Divider,
} from "@chakra-ui/react";
import { FaPaperPlane } from "react-icons/fa";

interface Props {
  isOpen: boolean;
  onClose: () => void;
}

export default function Support({ isOpen, onClose }: Props) {
  const messageRef = React.useRef<HTMLInputElement>(null);
  const [messages, setMessages] = React.useState<any>([]);

  const handleSendMessage = () => {
    const newMessage = messageRef.current?.value;
    setMessages([...messages, { message: newMessage, from: "user" }]);
    messageRef.current!.value = "";
    alert("Sorry, this feature is not implemented yet :(");
  };

  return (
    <>
      <Modal isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader
            textAlign={"center"}
            fontSize={"2xl"}
            fontWeight={"semibold"}
            bgGradient="linear(to-r, whatsapp.500, whatsapp.300, whatsapp.500)"
            bgClip="text"
          >
            Live chat with support
          </ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            <Divider orientation="horizontal" />
            <Flex
              h="500px"
              px={4}
              borderRadius="md"
              overflowY="scroll"
              flexDirection="column"
              __css={{
                "&::-webkit-scrollbar": {
                  width: "0.4em",
                },
                "&::-webkit-scrollbar-track": {
                  width: "0.4em",
                },
                "&::-webkit-scrollbar-thumb": {
                  backgroundColor: "whatsapp.500",
                  borderRadius: "24px",
                },
              }}
            >
              {messages.map((msg: any) =>
                msg.from === "support" ? (
                  <Flex
                    flexDirection={"row"}
                    alignItems={"center"}
                    justifyContent={"flex-start"}
                  >
                    <Flex
                      bg={"whatsapp.500"}
                      borderRadius={"md"}
                      p={2}
                      m={2}
                      maxW={"50%"}
                    >
                      <p>{msg.message}</p>
                    </Flex>
                  </Flex>
                ) : (
                  <Flex
                    flexDirection={"row"}
                    alignItems={"center"}
                    justifyContent={"flex-end"}
                  >
                    <Flex
                      bg={"whatsapp.300"}
                      borderRadius={"md"}
                      p={2}
                      m={2}
                      maxW={"50%"}
                    >
                      <p>{msg.message}</p>
                    </Flex>
                  </Flex>
                ),
              )}
            </Flex>
            <Flex
              flexDirection={"row"}
              alignItems={"center"}
              justifyContent={"center"}
              mt={2}
            >
              <Input
                placeholder="What's the issue?"
                w={"80%"}
                ref={messageRef}
                mx={2}
                onKeyDown={(e: any) => {
                  if (e.key === "Enter") {
                    handleSendMessage();
                  }
                }}
              />
              <IconButton
                aria-label="Send message"
                icon={<Icon as={FaPaperPlane} />}
                onClick={handleSendMessage}
              />
            </Flex>
          </ModalBody>
          <ModalFooter></ModalFooter>
        </ModalContent>
      </Modal>
    </>
  );
}
