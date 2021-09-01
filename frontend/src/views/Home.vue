<template>
  <div class="home">
    <div class="container">
      <div class="p-3">
        <table class="table">
          <thead class="thead-dark">
            <tr>
              <th scope="col">#</th>
              <th scope="col">Date</th>
              <th scope="col">Distance</th>
              <th scope="col">Duration</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(sp, index) in speed"
              :key="sp.pk"
              :index="index">
              <th scope="row">{{ index + 1 }}</th>
              <td>{{ sp.date }}</td>
              <td>{{ sp.distance }}</td>
              <td>{{ sp.duration }}</td>
            </tr>
          </tbody>
        </table>
    </div>
  <div>
    <p>Average Speed:</p>
  </div>
    </div>
  </div>
</template>

<script>
// import { apiService } from "../common/api.service"
export default {
  name: "Home",
  data() {
    return {
      speed: [],
    }
  },
  methods: {
    // getSpeedData() {
    //   let endpoint = "api/speed/";
    //   apiService(endpoint)
    //         .then(data => {
    //         this.speed.push(...data.results)
    //       })
    // }
  },
  async created() {
    var response = await fetch('http://127.0.0.1:8000/api/speed/');
    this.speed = await response.json();
  },};
</script>
