<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="/">Insurance Database</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <a class="nav-link" href="/">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            People
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <router-link to="/add-person" class="dropdown-item">Add</router-link>
            <a class="dropdown-item">All</a>
            <a class="dropdown-item">Search</a>
          </div>
        </li>
      </ul>
      <form method="POST" class="form-inline my-2 my-lg-0" action="">
        <input id="input" name="input" class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
        <button id="search" name="search" class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
      </form>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style scoped>

</style>
