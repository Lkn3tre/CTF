import React from "react";
import {
  Card,
  CardBody,
  CardFooter,
  Divider,
  Flex,
  Heading,
  Image,
  Stack,
  Text,
  Button,
  useToast,
  Box,
  useBreakpointValue,
} from "@chakra-ui/react";
import Navigation from "./Navigation";
import { instance } from "../../config/config";
import { useCookies } from "react-cookie";
import { Marquee } from "dynamic-marquee-react";

export function Banners() {
  const isMobile = useBreakpointValue({ base: false, md: true, lg: true });

  const images = ["/manhood.gif", "/hit.gif", "/hack.gif", "/moms.gif"];

  return isMobile ? (
    <Box
      display={{
        base: "none",
        md: "block",
      }}
      overflow="hidden"
      width="100%"
      position="relative"
    >
      <Marquee rate={200}>
        {images.map((image, index) => (
          <React.Fragment key={index}>
            <Box p={2} borderRadius="md" display="inline-block" width="300px">
              <Image src={image} alt={`Image ${index}`} width="100%" />
            </Box>
            {index < images.length - 1 && <Divider orientation="vertical" />}
          </React.Fragment>
        ))}
      </Marquee>
    </Box>
  ) : (
    <></>
  );
}

export default function Shop() {
  const [items, setItems] = React.useState<any>([]);
  const [cookie] = useCookies(["token"]);
  const toast = useToast();

  React.useEffect(() => {
    instance
      .get("/shop/items", {
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

  const handleBuy = (item: any) => {
    instance
      .post(
        "/shop/checkout",
        {
          id: item,
        },
        {
          headers: {
            Authorization: `Bearer ${cookie.token}`,
          },
        },
      )
      .then(() => {
        window.location.href = "/items";
      })
      .catch(() => {
        toast({
          title: "Error",
          description: "You are too broke to buy this item",
          status: "error",
          duration: 5000,
          isClosable: true,
        });
      });
  };
  return (
    <>
      <Navigation />
      <Banners />
      <Divider />
      <Flex
        alignItems={"center"}
        justifyContent={"center"}
        flexWrap={"wrap"}
        // p={'2rem'}
      >
        {items.map((item: any) => (
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
            border={"md"}
            borderColor={"whatsapp.500"}
            borderWidth={"1px"}
          >
            <CardBody>
              <Box h={"15rem"} flex={1}>
                <Image
                  src={item.image}
                  border={"md"}
                  overflow={"hidden"}
                  h={"250px"}
                  objectFit={"scale-down"}
                  alignSelf={"center"}
                />
              </Box>
              <Stack mt={"6"} spacing={"3"}>
                <Heading size={"md"}>{item.name}</Heading>
                <Text color="whatsapp.500" fontSize={"2xl"}>
                  {item.price} MAD
                </Text>
              </Stack>
            </CardBody>
            <Divider />
            <CardFooter>
              <Button
                colorScheme="whatsapp"
                variant="outline"
                onClick={() => handleBuy(item.id)}
              >
                Buy now
              </Button>
            </CardFooter>
          </Card>
        ))}
      </Flex>
    </>
  );
}
