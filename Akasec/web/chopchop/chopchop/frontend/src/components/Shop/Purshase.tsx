import React from "react";
import {
  Flex,
  Stack,
  Heading,
  Text,
  Image,
  Center,
  Box,
  Divider,
  IconButton,
  useDisclosure,
} from "@chakra-ui/react";
import { Card, CardBody } from "@chakra-ui/react";
import Navigation from "./Navigation";
import { AiOutlineMessage } from "react-icons/ai";
import Support from "../support/Support";
import { useCookies } from "react-cookie";
import { instance } from "../../config/config";

export default function PurshasedItems() {
  const [cookie] = useCookies(["token"]);
  const [items, setItems] = React.useState<any>([]);

  React.useEffect(() => {
    instance
      .get("/shop/orders", {
        headers: {
          Authorization: `Bearer ${cookie.token}`,
        },
      })
      .then((res) => {
        setItems(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  const { isOpen, onOpen, onClose } = useDisclosure();

  return (
    <Box position="relative">
      <Navigation />
      <Text
        textAlign={"center"}
        fontSize={"6xl"}
        fontWeight={"semibold"}
        bgGradient="linear(to-r, whatsapp.500, whatsapp.300, whatsapp.500)"
        bgClip="text"
      >
        Orders
      </Text>
      <Flex
        alignItems={"center"}
        justifyContent={"center"}
        flexWrap={"wrap"}
        p={"2rem"}
      >
        {items.length > 0 ? (
          items.map((item: any) => (
            <Card
              maxW="sm"
              margin={2}
              shadow={"lg"}
              w={"40rem"}
              _hover={{
                transform: "scale(1.02)",
                transition: "all 0.1s ease-in-out",
              }}
              h={"30rem"}
            >
              <CardBody>
                <Box h={"50%"}>
                  <Image src={item.image} border={"md"} alignSelf={"center"} />
                </Box>
                <Stack mt={"6"} spacing={"3"}>
                  <Heading size={"md"}>{item.name}</Heading>
                  <Divider w="100%" />
                  <Box>
                    <Text color="messenger.500" fontSize={"md"}>
                      Order info:
                    </Text>
                    <Text>{item.Content}</Text>
                  </Box>
                </Stack>
              </CardBody>
            </Card>
          ))
        ) : (
          <Center flexDirection={"column"} alignContent={"center"}>
            <Text fontSize={"2xl"}>You have no items yet</Text>
            <Text fontSize={"2xl"} fontStyle={"italic"}>
              Explore our shop and get yourself something nice, you know you
              deserve it
            </Text>
          </Center>
        )}
      </Flex>
      <IconButton
        position="fixed"
        bottom={4}
        right={4}
        borderRadius={"full"}
        icon={<AiOutlineMessage size={50} />}
        aria-label={"Contact support"}
        onClick={onOpen}
        mb={4}
      />
      <Support isOpen={isOpen} onClose={onClose} />
    </Box>
  );
}
