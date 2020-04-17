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
      <img src="../assets/cloud.png" />
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

