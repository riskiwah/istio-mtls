<template>
  <div class="card">
    <h2>{{ weather.name }}</h2>
    <h3>
      {{ weather.weather[0].main }}
      <span>
        {{ weather.wind.speed }} km/h
        <span class="dot">-</span>
        {{ weather.weather[0].description }}
      </span>
    </h3>
    <h1>{{ weather.main.temp }}&degC</h1>
    <div class="line1"></div>
    <div class="corner-right">
      <img src="https://www.dropbox.com/s/w4eods8cj3qc2z7/cloud.png?raw=1" />
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  async asyncData() {
    const { data } = await axios.get(process.env.baseUrl + "/api/cuaca");
    return { weather: data };
  }
};
</script>

