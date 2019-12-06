<template>
  <div class="container">
    <div>
      <logo />
      <h1 class="title">
        {{ weather.location.name }},
        {{ weather.location.region }}, Indonesia
      </h1>
      <v-card class="mx-auto" min-height="300" raised>
        <v-list-item three-line>
          <v-list-item-content>
            <div class="raised mb-4">{{ weather.current.temperature }}° Celcius</div>
            <v-list-item-title class="headline mb-1">Headline 5</v-list-item-title>
            <v-list-item-subtitle>Greyhound divisely hello coldly fonwderfully</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-card>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  async asyncData () {
    const { data } = await axios.get(process.env.baseUrl +'/api/cuaca')
    return { weather: data }
  },
}

</script>

<style>
.container {
  margin: 0 auto;
  min-height: 50vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 80px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 3px;
  padding-bottom: 15px;
}

.raised {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 250;
  font-size: 60px;
  color: #35495e;
}
</style>
