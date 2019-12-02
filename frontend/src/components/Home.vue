<template>
  <div class="site-wrap">

    <div class="site-mobile-menu site-navbar-target">
      <div class="site-mobile-menu-header">
        <div class="site-mobile-menu-close mt-3">
          <span class="icon-close2 js-menu-toggle"></span>
        </div>
      </div>
      <div class="site-mobile-menu-body"></div>
      </div> <!-- .site-mobile-menu -->
    <!-- NAVBAR -->
    <header class="site-navbar mt-3">
      <div class="container-fluid">
        <div class="row align-items-center">
          <div class="site-logo col-6"><a href="/">Careers</a></div>

          <nav class="mx-auto site-navigation">
            <ul class="site-menu js-clone-nav d-none d-xl-block ml-0 pl-0">
              <li><a href="/" class="nav-link active">Trang chủ</a></li>
              <!-- <li><a href="job-listings.html">Danh sách việc làm</a></li> -->
            </ul>
          </nav>
        </div>
      </div>
    </header>

    <!-- HOME -->
    <section class="home-section section-hero overlay bg-image" style="background-image: url('images/hero_1.jpg');" id="home-section">
      <div class="container">
        <div class="row align-items-center justify-content-center">
          <div class="col-md-12">
            <div class="mb-5 text-center">
              <h1 class="text-white font-weight-bold">Website Tìm Việc Làm</h1>
              <p>Tìm kiếm công việc bạn mong muốn</p>
            </div>
            <form method="post" class="search-jobs-form">
              <div class="row mb-5">
                <div class="col-12 col-sm-6 col-md-6 col-lg-6 mb-4 mb-lg-0">
                  <input type="text"
                    class="form-control form-control-lg"
                    placeholder="Tên công việc, keywords..."
                    v-model="description"
                    />
                </div>
                <div class="col-12 col-sm-6 col-md-6 col-lg-2 mb-4 mb-lg-0">
                  <input type="text"
                    class="form-control form-control-lg"
                    placeholder="Nơi làm việc"
                    v-model="address"
                  />
                </div>
                <div class="col-12 col-sm-6 col-md-6 col-lg-2 mb-4 mb-lg-0">
                  <input type="text"
                    class="form-control form-control-lg"
                    placeholder="Mức lương mong muốn"
                    v-model="salary"
                  />
                </div>
                <div class="col-12 col-sm-6 col-md-6 col-lg-2 mb-4 mb-lg-0">
                  <button type="button"
                    class="btn btn-primary btn-lg btn-block text-white btn-search"
                    v-on:click="searchJob()"
                  >
                    <span class="icon-search icon mr-2"></span>
                      Tìm việc
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data: () => ({
    description: null,
    address: null,
    salary: null
  }),
  methods: {
    searchJob() {
      window.location = `/search?description=${this.description}&address=${this.address}&salary=${this.salary}`
    }
  }
}
</script>