<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
        <div class="container">
             <router-link
                :to="{ name: 'Home' }"
                class="navbar-brand"
                >ReportPage 
            </router-link>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <router-link
                        :to="{ name: 'Home' }"
                        class="nav-link"
                      >Home  
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link
                        :to="{ name: 'add-data' }"
                        class="nav-link"
                      >+Add  
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link
                        :to="{ name: 'Report' }"
                        class="nav-link"
                      >Report  
                    </router-link>
                </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/accounts/logout/">Logout</a>
                    </li>
                </ul>
                <form class="form-inline my-2 my-lg-0">
                <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search" disabled>
                <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                </form>
            </div>
        </div>
    </nav>
</template>

<script>
export default{
    name: "NavbarComponent"
}
</script>

<style>
    .my-navbar {
        border-bottom: 1px solid #DDD;
    }
    .navbar-brand {
        font-weight: bold;
        font-size: 130%;
    }
    .navbar-brand:hover {
        color: #DC3545 !important
    }
</style>