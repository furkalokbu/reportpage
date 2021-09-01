import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Report from "../views/Report.vue";
import UserEditor from "../views/UserEditor.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/report",
    name: "Report",
    component: Report, 
  },
  {
    path: "/add",
    name: "add-data",
    component: UserEditor,
  },
];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes,
});

export default router;
