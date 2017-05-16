const APP_NAME = 'plataforma';

// TODO: 2. Run these in shell
// npm init -f
// npm install gulp gulp-autoprefixer gulp-clean-css gulp-image-optimization gulp-rename gulp-sass gulp-watch gulp-uglify gulp-notify pump --save
// gulp

var gulp = require('gulp');
var sass = require('gulp-sass');
var prefix = require('gulp-autoprefixer');
var rename = require('gulp-rename');
var watch = require('gulp-watch');
var imageop = require('gulp-image-optimization');
var cleanCSS = require('gulp-clean-css');
var uglify = require('gulp-uglify');
var pump = require('pump');
var notify = require('gulp-notify');

var basePath = APP_NAME + '/static/';
var scssPath = basePath + 'dev/scss/*.scss';
var cssDest = basePath + 'css';

var imagesPath = basePath + 'dev/img/**/*';
var imagesDest = basePath + 'img';

var jsPath = basePath + 'dev/js/*.js';
var jsDest = basePath + 'dist';

/* Images */
gulp.task('images', function (cb) {
  notify().write('Gulp Images Started');
  gulp.src(imagesPath)
      .pipe(imageop({
          optimizationLevel: 10,
          progressive: true,
          interlaced: true
      }))
      .pipe(gulp.dest(imagesDest))
      .on('end', cb)
      .on('error', cb);
});

/* Styles */
gulp.task('style', function () {
  gulp.src(scssPath)
      .pipe(sass().on('error', sass.logError))
      .on('error', notify.onError(function (error) {
        return 'Error on SASS/SCSS.\nLook in the console for details.\n';
      }))
      .pipe(prefix({
        browsers: ['IE 8', 'IE 9', 'last 5 versions', 'Firefox 14', 'Opera 11.1'],
        cascade: false
      }))
      .pipe(cleanCSS())
      .pipe(rename({suffix: '.min'}))
      .pipe(gulp.dest(cssDest))
      .pipe(notify('Gulp Style Done'));
});

/* Scripts Compress */
gulp.task('compress', function (cb) {
  pump([
        gulp.src(jsPath)
        .pipe(rename({suffix: '.min'})),
        uglify()
        .on('error', notify.onError(function (error) {
          return 'Error on JS.\nLook in the console for details.\n';
        })),
        gulp.dest(jsDest)
        .on('end', function(){
          notify().write('Gulp JS Done')
        })
      ],
      cb
  );
});

/* Watch Routine */
gulp.task('watch', function () {
  gulp.watch(scssPath, ['style']);
  gulp.watch(jsPath, ['compress']);
  gulp.watch(imagesPath, ['images']);
});

/* Default */
gulp.task('default', ['images', 'style', 'compress', 'watch']);
