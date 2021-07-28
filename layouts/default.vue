<template>
  <div>
    <div id="header">
      <span>New England Treasures</span>
      <nav>
        <NuxtLink to="/" aria-label="Map">
          <img src="~/assets/map_icon.svg" style="width: 30px; height: 30px;" /><span>Map</span>
        </NuxtLink>
        <NuxtLink to="/list" aria-label="List">
          <img src="~/assets/list-ul.svg" style="width: 30px; height: 30px;" /><span>List</span>
        </NuxtLink>
        <NuxtLink to="/search" aria-label="Search">
          <img src="~/assets/search.svg" style="width: 30px; height: 30px;" /><span>Search</span>
        </NuxtLink>
      </nav>
    </div>
    <Nuxt />
  </div>
</template>

<style>
html,
body,
#__nuxt,
#__layout,
#__layout > div {
  width: 100%;
  height: 100%;
  margin: 0;
  background-color: #bddab1;
}

html {
  font-family:
    'Source Sans Pro',
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    'Helvetica Neue',
    Arial,
    sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
}

.button--green {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #3b8070;
  color: #3b8070;
  text-decoration: none;
  padding: 10px 30px;
}

.button--green:hover {
  color: #fff;
  background-color: #3b8070;
}

.button--grey {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #35495e;
  color: #35495e;
  text-decoration: none;
  padding: 10px 30px;
  margin-left: 15px;
}

.button--grey:hover {
  color: #fff;
  background-color: #35495e;
}

#header {
  width: 100%;
  display: block;
  background: #fff;
  vertical-align: middle;
  top: 0;
  border-bottom: 2px solid #228b22;
}

nav {
  display: inline-block;
  vertical-align: middle;
  padding: 5px 0;
}

nav > a {
  color: #000;
  text-decoration: none;
  margin-left: 25px;
  padding: 3px;
  display: inline-block;
  vertical-align: middle;
  border-style: solid;
  border-width: 1px;
  border-color: #fff;
  position: relative;
}

nav > a:hover {
  border-color: #228b22;
  border-radius: 5px;
  color: #000;
}

nav > a.nuxt-link-exact-active {
  border-color: #228b22;
  border-radius: 5px;
  background-color: #bddab1;
  text-decoration: underline;
}

nav > a > span {
  margin-left: 5px;
}

#header > span {
  color: #228b22;
  font-size: 25px;
  display: inline-block;
  vertical-align: middle;
  padding: 5px 0 5px 25px;
}
</style>
