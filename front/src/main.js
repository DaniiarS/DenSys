import { createApp } from "vue";
import { createWebHistory, createRouter } from "vue-router";

// styles

// import "@/assets/styles/tailwind.css";
import "@/output.css";
import "@fortawesome/fontawesome-free/css/all.min.css";

// mouting point for the whole app

import App from "@/App.vue";

// layouts

import Admin from "@/layouts/AdminLayout.vue";
import Auth from "@/layouts/AuthLayout.vue";

// views for Admin layout

import PatientRegister from "@/components/PatientRegister.vue";
import Dashboard from "@/views/admin/DashboardPage.vue";
import Settings from "@/views/admin/SettingsPage.vue";
import Tables from "@/views/admin/TablesPage.vue";
import Maps from "@/views/admin/MapsPage.vue";

// views for Auth layout

import Login from "@/views/auth/LoginPage.vue";
import Register from "@/views/auth/RegisterPage.vue";

// views without layouts

import Landing from "@/views/LandingPage.vue";
import Profile from "@/views/ProfilePage.vue";
import Index from "@/views/IndexPage.vue";

// routes

const routes = [
  {
    path: "/admin",
    component: Admin,
    children: [
      {
        path: "/admin/patient-register",
        component: PatientRegister,
      },
      {
        path: "/admin/dashboard",
        component: Dashboard,
      },
      {
        path: "/admin/settings",
        component: Settings,
      },
      {
        path: "/admin/tables",
        component: Tables,
      },
      {
        path: "/admin/maps",
        component: Maps,
      },
    ],
  },
  {
    path: "/auth",
    redirect: "/auth/login",
    component: Auth,
    children: [
      {
        path: "/auth/login",
        component: Login,
      },
      {
        path: "/auth/register",
        component: Register,
      },
    ],
  },
  {
    path: "/landing",
    component: Landing,
  },
  {
    path: "/profile",
    component: Profile,
  },
  {
    path: "/",
    component: Index,
  },
  { path: "/:pathMatch(.*)*", redirect: "/" },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

createApp(App).use(router).mount("#app");
