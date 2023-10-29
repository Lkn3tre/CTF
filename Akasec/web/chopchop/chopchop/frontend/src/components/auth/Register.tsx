import React from "react";
import {
  Button,
  Flex,
  Container,
  Divider,
  Heading,
  Input,
  Stack,
  Text,
  Alert,
  AlertIcon,
  AlertTitle,
} from "@chakra-ui/react";
import { instance } from "../../config/config";
import { useColorMode } from "@chakra-ui/color-mode";

export default function Register() {
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [username, setUsername] = React.useState("");
  const [err, setErr] = React.useState("");
  const colorMode = useColorMode();

  let mColor = colorMode.colorMode === "light" ? "white" : "gray.700";

  const handleSumbit = () => {
    setErr("");
    instance
      .post("/auth/register", {
        email: email,
        name: username,
        password: password,
      })
      .then(() => {
        window.location.href = "/login";
      })
      .catch((err) => {
        if (typeof err.response.data === "string") {
          setErr(err.response.data);
        } else {
          setErr(err.response.data.message[0]);
        }
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
        <Heading as="h1" size="lg" mb={3}>
          Register
        </Heading>
        <Text mb={4}>
          Welcome to the ChopChop shop! Please register to continue.
        </Text>

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
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <Input
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            type="password"
          />
          <Divider my={2} />
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
            Sign up
          </Button>
        </Stack>
      </Container>
    </Flex>
  );
}
