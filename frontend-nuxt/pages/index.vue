<template>
  <div class="container-fluid">
    <div>
      <logo />

      <div class="row p-3 justify-content-md-center text-center">
        <div class="col-md-6 side-bar">
          <!-- our title part----------------------->
          <h1 class="title text-light mb-5">Weather App</h1>

          <!-- form part----------------------->
          <form>
            <div class="form-group">
              <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter a city">
            </div>
            <button type="submit" class="btn btn-danger btn-block">GET WEATHER</button>
          </form>
        </div>

        <div class="col-md-6 content-bar">
          <!-- location result----------------------->
          <div class="row justify-content-md-center dat-table-grip">
            <h3> Sleman, Indonesia </h3>
          </div>

          <!-- part result----------------------->
          <div class="row justify-content-md-center dat-table-grip">bb</div>


          <!-- weather result----------------------->
          <div class="row justify-content-md-center dat-table-grip p-5">
            <h1 class="title">
              63° Celcius
            </h1>
          </div>
        
        </div>
      </div>
      
      <!-- <h1 class="title">
        Sleman,
        Jogja, Indonesia
      </h1>
      <v-card class="mx-auto" min-height="300" raised>
        <v-list-item three-line>
          <v-list-item-content>
            <div class="raised mb-4">° Celcius</div>
            <v-list-item-title class="headline mb-1">Headline 5</v-list-item-title>
            <v-list-item-subtitle>Greyhound divisely hello coldly fonwderfully</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-card> -->
    </div>
  </div>
</template>

<script>
// import axios from 'axios'

// export default {
//   async asyncData () {
//     const { data } = await axios.get(process.env.baseUrl +'/api/cuaca')
//     return { weather: data }
//   },
// }

</script>

<style>

.side-bar, .content-bar{
  min-height: 95vh
}

.side-bar{
  background-color: #f66161;
  padding: 10rem 5rem 8rem 5rem;
}

.dat-table-grip{
  min-height: 33%;
  color: rgb(12, 208, 188) !important;
}

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
