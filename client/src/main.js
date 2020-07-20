import App from "./App.svelte";

const app = new App({
  target: document.body,
  props: {
    name: "world",
    temp: "0",
    humidity: "0",
    time: "00:00",
  },
});

export default app;
