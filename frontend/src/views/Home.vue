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
    <p>Average Speed: {{ aver_speed }}</p>
  </div>
    </div>
    <div class="container">
  <footer class="py-5">
    <div class="d-flex justify-content-between py-4 my-4 border-top">
      <p>&copy; 2021 Company, Inc. All rights reserved.</p>
      <ul class="list-unstyled d-flex">
        <li class="ms-3"><a class="link-dark" href="#"><svg class="bi" width="24" height="24"><use xlink:href="#twitter"/></svg></a></li>
        <li class="ms-3"><a class="link-dark" href="#"><svg class="bi" width="24" height="24"><use xlink:href="#instagram"/></svg></a></li>
        <li class="ms-3"><a class="link-dark" href="#"><svg class="bi" width="24" height="24"><use xlink:href="#facebook"/></svg></a></li>
      </ul>
    </div>
  </footer>
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
      aver_speed: [],
    }
  },
  methods: {
  },
  async created() {
    var response = await fetch('http://127.0.0.1:8000/api/speed/');
    this.speed = await response.json();
    this.aver_speed = this.speed[0].average_speed;
    console.log(this.speed);
  },};
</script>
