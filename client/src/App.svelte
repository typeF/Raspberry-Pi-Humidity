<script>
  import { onMount } from "svelte";
  import axios from "axios";

  export let name;
  export let temp;
  export let time;
  export let humidity;

  onMount(async () => {
    const res = await axios
      .get("/api/records")
      .catch(err => console.error(err));

    humidity = res.data.readings[0].humidity;
    temp = res.data.readings[0].temperature;
  });

  function getLatestReading() {
    return axios
      .get("/api/records")
      .then(res => {
        humidity = res.data.readings[0].humidity;
        temp = res.data.readings[0].temperature;
      })
      .catch(err => console.error(err));
  }
</script>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    height: 100%;
  }

  h1 {
    color: #41c2aa;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 300;
  }

  .field {
    font-weight: 200;
    font-size: 80px;
    margin: 0;
    text-align: right;
    width: 100%;
    font-family: "Major Mono Display", monospace;
  }

  .field-unit {
    font-size: 40px;
    font-weight: 140;
    margin: 0;
    text-align: left;
  }

  .subfield {
    margin-top: 0;
    color: grey;
    text-align: left;
  }

  .field-container {
    display: flex;
    align-items: end;
    justify-content: center;
  }

  .field-sub-container {
    display: grid;
    grid-template-columns: 5fr 3fr;
    width: 400px;
  }

  .field-label-container {
    display: flex;
    flex-direction: column;
    justify-content: end;
    padding: 0 0 0 10px;
  }

  .time-field {
    font-size: 49px;
  }

  .date-field {
    font-size: 25px;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>

<svelte:head>
  <link
    href="https://fonts.googleapis.com/css2?family=Major+Mono+Display&display=swap"
    rel="stylesheet" />
</svelte:head>

<main>
  <div class="field-container">
    <div class="field-sub-container">
      <p class="field">{temp}</p>
      <div class="field-label-container">
        <p class="field-unit">C</p>
        <p class="subfield">TEMP</p>
      </div>
    </div>
  </div>
  <div class="field-container">
    <div class="field-sub-container">
      <p class="field">{humidity}</p>
      <div class="field-label-container">
        <p class="field-unit">%</p>
        <p class="subfield">HUMIDITY</p>
      </div>
    </div>
  </div>
  <div class="field-container">
    <div class="field-sub-container">
      <p class="field time-field">12:37</p>
      <div class="field-label-container">
        <p class="field-unit date-field">JUL 1</p>
        <p class="subfield">LAST UPDATE</p>
      </div>
    </div>
  </div>
</main>
