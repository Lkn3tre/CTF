import React from "react";
import {
  Button,
  Flex,
  Container,
  Divider,
  Heading,
  Input,
  Link,
  Stack,
  Text,
  Alert,
  AlertIcon,
  AlertTitle,
} from "@chakra-ui/react";
import { instance } from "../../config/config";
import { useCookies } from "react-cookie";
import { useColorMode } from "@chakra-ui/color-mode";

export default function Login() {
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [err, setErr] = React.useState("");
  const [, setCookie] = useCookies(["token"]);
  const colorMode = useColorMode();

  let mColor = colorMode.colorMode === "light" ? "white" : "gray.700";

  const handleSumbit = () => {
    setErr("");
    instance
      .post("/auth/login", {
        email: email,
        password: password,
      })
      .then((res) => {
        setCookie("token", res.data.token, { path: "/" });
        // Use history.push to navigate to the home page after successful login
        window.location.href = "/";
      })
      .catch(() => {
        setErr("Invalid email or password");
      });
  };

  return (
    <Flex
      alignItems={"center"}
      justifyContent={"center"}
      minHeight="100vh" // Center vertically on the screen
    >
      <Container
        maxW="container.sm"
        bg={mColor}
        borderRadius={10}
        mt={1}
        boxShadow={"dark-lg"}
        p={6}
        textAlign="center" // Center the contents horizontally
      >
        <Heading as="h1" size="lg" mb={6}>
          Login
        </Heading>
        {err && (
          <Alert status="error" mb={4}>
            <AlertIcon />
            <AlertTitle mr={2}>{err}</AlertTitle>
          </Alert>
        )}
        <Stack
          direction="column"
          spacing={4} // Increased spacing between elements for aesthetics
        >
          <Input
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <Input
            placeholder="Password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <Button
            colorScheme="messenger"
            variant="solid"
            mt={2}
            onClick={handleSumbit}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                handleSumbit();
              }
            }}
          >
            Login
          </Button>
          <Divider my={2} />
          <Text>
            Don't have an account?{" "}
            <Link color="messenger.500" href="/register">
              Sign up
            </Link>
          </Text>
        </Stack>
      </Container>
    </Flex>
  );
}
