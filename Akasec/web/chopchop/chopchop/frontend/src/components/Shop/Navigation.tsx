import {
  Box,
  Container,
  Spacer,
  Flex,
  Button,
  useDisclosure,
  Text,
  Menu,
  MenuButton,
  MenuList,
  MenuItem,
  Divider,
  VStack,
  HStack,
} from "@chakra-ui/react";
import React from "react";
import { AiOutlineShop, AiOutlineLogout } from "react-icons/ai";
import { instance } from "../../config/config";
import { useCookies } from "react-cookie";
import { MdAccountBalanceWallet } from "react-icons/md";
import { FaUserCircle } from "react-icons/fa";
import { useColorMode } from "@chakra-ui/color-mode";
import Redeem from "./Redeem";

export default function Navigation() {
  const colorMode = useColorMode();
  const { isOpen, onOpen, onClose } = useDisclosure();
  const [user, setUser] = React.useState<any>();
  const [cookies, removeCookie] = useCookies(["token"]);

  let navColor = colorMode.colorMode === "light" ? "white" : "gray.700";

  React.useEffect(() => {
    const token = cookies.token;
    instance
      .get("/shop/me", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      .then((res: any) => {
        setUser(res.data);
      })
      .catch((err: any) => {
        console.log(err);
      });

    instance
      .get("/shop/isAdmin", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
      .then(() => {
        setUser((prev: any) => {
          return {
            ...prev,
            isAdmin: true,
          };
        });
      })
      .catch(() => {
        console.log(":(");
      });
  }, [cookies.token]);

  return (
    <Box
      as="nav"
      role="navigation"
      aria-label="main navigation"
      bg={navColor}
      borderRadius={10}
      mt={1}
      boxShadow={"lg"}
    >
      <Container maxW="container.xl">
        <Flex alignItems="center" py="4">
          <Flex color="whatsapp.500" flexDirection={"row"}>
            <AiOutlineShop size={30} />
            <Text fontSize="xl" fontWeight="semibold" letterSpacing="wide">
              ChopChop!
            </Text>
          </Flex>
          <Divider
            orientation="vertical"
            colorScheme="messenger"
            h="40px"
            mx="2"
          />
          <Box display="flex" alignItems="center">
            <Box
              as="a"
              href="/"
              mr="4"
              _hover={{
                color: "messenger.500",
              }}
            >
              Home
            </Box>
            <Box
              as="a"
              href="/items"
              mr="4"
              _hover={{
                color: "messenger.500",
              }}
            >
              My Items
            </Box>
          </Box>
          <Spacer />
          {user ? (
            <Box
              display="flex"
              alignItems="center"
              borderColor={"whatsapp.500"}
            >
              <Menu>
                <MenuButton
                  aria-label="Options"
                  borderColor="messenger.500"
                  pr={2}
                >
                  <HStack>
                    <Box color={"whatsapp.300"}>
                      <FaUserCircle size={35} />
                    </Box>
                    <VStack
                      alignItems="flex-start"
                      spacing="1px"
                      overflow="hidden"
                    >
                      <Text
                        fontSize="sm"
                        fontWeight="bold"
                        color="whatsapp.500"
                      >
                        {" "}
                        {user.username}
                      </Text>
                      <Text fontSize="xs" color="gray.500">
                        Balance: {user.balance} DH
                      </Text>
                    </VStack>
                  </HStack>
                </MenuButton>
                <MenuList>
                  <MenuItem
                    icon={<AiOutlineLogout />}
                    onClick={() => {
                      removeCookie("token", { path: "/" });
                      window.location.reload();
                    }}
                  >
                    Log out
                  </MenuItem>
                  {user.isAdmin && (
                    <MenuItem
                      icon={<MdAccountBalanceWallet />}
                      onClick={onOpen}
                    >
                      Redeem Voucher
                    </MenuItem>
                  )}
                </MenuList>
              </Menu>
            </Box>
          ) : (
            <Box display="flex" alignItems="center">
              <Button
                colorScheme="messenger"
                variant="outline"
                mr="4"
                onClick={() => {
                  removeCookie("token", { path: "/" });
                  window.location.href = "/login";
                }}
              >
                Login
              </Button>
              <Button
                colorScheme="messenger"
                onClick={() => {
                  window.location.href = "/register";
                }}
              >
                Sign Up
              </Button>
            </Box>
          )}
        </Flex>
      </Container>
      <Redeem isOpen={isOpen} onClose={onClose} />
    </Box>
  );
}
