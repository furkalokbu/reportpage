<template>
  <div class="container">
          <div class="p-3">
        <table class="table">
          <thead class="thead-dark">
            <tr>
              <th scope="col">#</th>
              <th scope="col">Distance</th>
              <th scope="col">Duration</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(sp, index) in speed"
              :key="sp.pk"
              :index="index">
              <th scope="row">{{ index + 1 }}</th>
              <td>{{ sp.distance }}</td>
              <td>{{ sp.duration }}</td>
            </tr>
          </tbody>
        </table>
    </div>
  </div>
</template>

<script>
// import { apiService } from "../common/api.service"
export default {
  name: "Report",
  data() {
    return {
      speed: [],
    }
  },
  methods: {
  },
  async created() {
    var response = await fetch('http://127.0.0.1:8000/api/report/?group_by=week');
    this.speed = await response.json();
    console.log(this.speed);
  },};
</script>
