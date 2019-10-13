<template>
  <div class="content">
    <header class="main-container">
      <div class="name-logo">
        <svg
          xmlns:svg="http://www.w3.org/2000/svg"
          viewBox="0 0 1171 100"
          id="knCompanyName_895defd3265d1d1a7e6413d57b1424dd"
        >
          <path
            style="fill:rgb(0, 43, 85)"
            d="m946.4-0.01172c-29.2 0-45.8 21.96-45.8 50.01 0 28.04 15.2 50 46.1 50 22 0 35.9-9.21 40.3-13.3v-41.91h-39v17.96h15.7v13.77c-2.6 1.91-8.2 3.86-15.8 3.86-17.5 0-22.8-15.85-22.8-30.38 0-14.54 4.3-30.38 20.8-30.38 8.5 0 13.1 5.32 15.4 12.23h24.7c-3.7-21.91-21.4-31.86-39.6-31.86zm-747.9 3.098v93.69h70.6v-19.99h-46.2v-18.85h38.6v-18.9h-38.6v-16.74h44.2v-19.21l-68.6-0.004zm-198.5 0.066v93.69h24.95v-26.48l9.08-11.02 20.97 37.5h29.52l-34.98-56.32 30.8-37.37-28.12 0.002-27.27 36.89v-36.89l-24.95 0.002zm94.07 0v55.32c0 27.16 12.43 40.67 40.83 40.67 28.3 0 40.8-13.51 40.8-40.67v-55.32l-24.4 0.002v57.09c0 12.07-4.5 18.25-16.4 18.25-12 0-16.4-6.18-16.4-18.25v-57.09l-24.43 0.002zm193.8 0v93.69h24.4v-38.91h32.1v38.91h24.5v-93.69l-24.5 0.002v34.46h-32.1v-34.46l-24.4 0.002zm107.9 0v93.69h22.9v-58.87l32.8 58.87h25.1v-93.69l-23 0.002v58.19l-32.8-58.19-25 0.002zm107.7 0v93.69h70.6v-19.99h-46.2v-18.85h38.6v-18.89h-38.6v-16.74h44.3v-19.22l-68.7 0.002zm198 0v93.69h23v-58.87l32.8 58.87h25v-93.69l-22.9 0.002v58.19l-32.8-58.19-25.1 0.002zm129.8 0l-37.7 93.69h25.1l6.3-17.46h36.6l6.1 17.46h27.2l-37.7-93.69-22.5 0.002h-3.4zm179.7 0v93.69h71v-19.99h-46v-18.85h38v-18.89h-38v-16.74h44v-19.22l-69 0.002zm93 0v93.69h67v-19.99h-43v-73.7l-24 0.002zm-260.6 24.75l11.8 33.37h-23.7l11.9-33.37z"
          />
          <path
            style="fill:rgb(86, 183, 233)"
            d="m644.2 96.84h-14.14v-37.14h-36.63v-13.12h36.63v-37.14h14.14v37.14h36.63v13.12h-36.63v37.14"
          />
        </svg>
      </div>

      <div class="side-pannel">
        <nav>
          <ul>
            <router-link to="/" exact tag="li">Home</router-link>
            <router-link to="register" tag="li">Register</router-link>
            <router-link to="list" tag="li">List</router-link>
            <!-- <router-link to="retrive" tag="li">Retrive</router-link> -->
          </ul>
        </nav>

        <div class="circle-logo">
          <svg
            xmlns:svg="http://www.w3.org/2000/svg"
            viewBox="0 0 102.5 100"
            id="knLogo_9cd9491381bc938975dcb42607e76ce0"
          >
            <path
              style="fill:rgb(86, 183, 233)"
              d="m10.05 50.05c0 10.15 3.674 19.44 9.764 26.62l-6.355 7.106c-8.332-8.89-13.42-20.73-13.42-33.73 0-27.59 22.9-49.95 51.16-49.95s51.16 22.36 51.16 49.95c0 13-5.084 24.84-13.42 33.72l-6.355-7.106c6.09-7.176 9.764-16.46 9.764-26.62 0-22.73-18.42-41.15-41.15-41.15s-41.15 18.42-41.15 41.15"
            />
            <path
              style="fill:rgb(0, 43, 85)"
              d="m46.72 33.56c0 2.474 2.007 4.48 4.481 4.48s4.481-2.006 4.481-4.48c0-2.478-2.007-4.484-4.481-4.484s-4.481 2.006-4.481 4.484zm-8.529 11.21h7.993v-0.9829c-3.902-1.827-6.596-5.721-6.596-10.23 0-6.263 5.199-11.34 11.61-11.34 6.412 0 11.61 5.076 11.61 11.34 0 4.505-2.693 8.399-6.595 10.23v0.9829h7.993v6.117h-7.993v40.01c7.848-0.9538 15.01-4.118 20.86-8.849l6.038 7.042c-8.748 6.827-19.84 10.91-31.91 10.91s-23.16-4.079-31.91-10.91l6.039-7.042c5.845 4.731 13.01 7.895 20.86 8.849v-40.01h-7.993v-6.117"
            />
          </svg>
        </div>
      </div>
    </header>
  </div>
</template>


<script>
export default {};
</script>


<style lang="scss" scoped>
@import "@/main.scss";

.content {
  border-bottom: 2px solid $baseColor;
}

header {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  padding-bottom: 8px;
  padding-top: 8px;

  .name-logo {
    width: 300px;
    margin-right: auto;
    margin-top: 8px;

    svg {
      width: 100%;
    }
  }

  .side-pannel {
    display: contents;
  }

  nav {
    display: inline-block;

    ul {
      list-style: none;

      li {
        display: inline-block;
        cursor: pointer;
        font-size: 1.5em;
        font-weight: bold;
        color: $baseColor;
        padding-left: 5px;
        padding-right: 5px;
        margin-left: 10px;
        margin-right: 10px;

        &:first-child {
          margin-left: 0px;
        }

        &:last-child {
          margin-right: 90px;
        }

        &:hover {
          color: $accentColor;
        }

        &.router-link-active {
          color: $accentColor;
          border-bottom: 2px solid $accentColor;
        }
      }
    }
  }

  .circle-logo {
    height: 50px;

    svg {
      height: 100%;
    }
  }
}
</style>
