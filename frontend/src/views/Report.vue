<template>
  <div class="container">
          <div class="p-3">
        <table class="table">
          <thead class="thead-dark">
            <tr>
              <th scope="col">Week</th>
              <th scope="col">Distance</th>
              <th scope="col">Duration</th>
              <th scope="col">Average</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in reports"
              :key="item.pk"
              :index="index">
              <th scope="row">{{ index + 1 }}</th>
              <td>{{ item.sum_dist }}</td>
              <td>{{ item.sum_dur }}</td>
              <td>{{ item.avg }}</td>
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
      reports: [],
    }
  },
  methods: {
  },
  async created() {
    var response = await fetch('http://127.0.0.1:8000/api/report/');
    this.reports = await response.json();
    console.log(this.speed);
  },};
</script>
