import React from "react";
import { ChakraProvider, extendTheme } from "@chakra-ui/react";
import { Route } from "react-router-dom";
import Shop from "./components/Shop/Shop";
import Login from "./components/auth/Login";
import Register from "./components/auth/Register";
import PurshasedItems from "./components/Shop/Purshase";

const theme = extendTheme({
  initialColorMode: "dark",
  useSystemColorMode: false,
  defaultColorMode: "dark",
  fonts: {
    heading: "Comic Sans MS",
    body: "Comic Sans MS",
  },
});

function App() {
  React.useEffect(() => {
    if (localStorage.getItem("chakra-ui-color-mode") !== "dark") {
      localStorage.setItem("chakra-ui-color-mode", "dark");
      window.location.reload();
    }
  }, []);

  return (
    <ChakraProvider theme={theme}>
      <Route exact path="/" component={Shop} />
      <Route exact path="/login" component={Login} />
      <Route exact path="/register" component={Register} />
      <Route exact path="/items" component={PurshasedItems} />
    </ChakraProvider>
  );
}

export default App;
