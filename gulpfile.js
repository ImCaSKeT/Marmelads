const {src, dest, watch, series, lastRun, parallel} = require("gulp");

var gulp = require('gulp'),                 // Сообственно Gulp JS
    pug = require('gulp-pug'),              // Плагин для Pug
    less = require('gulp-less'),            // Плагин для LESS
    autoprefixer = require('gulp-autoprefixer'),
    rename = require("gulp-rename"),
    sourcemaps = require('gulp-sourcemaps'),// Плагин для карты стилий
    csso = require('gulp-csso'),            // Плагин для Минификации
    uglify = require('gulp-uglify'),        // Минификация JS
    concat = require('gulp-concat');        // Плагин для Сервера
    browserSync = require('browser-sync');  // Подключаем Browser Sync




// Таск для работы с шаблонами
gulp.task('pug', function () {
    return gulp.src(['./app//**/*.pug', '!./app//**/_*.pug'], { since: lastRun(pug) })
    .pipe(pug({pretty: true}))
    .pipe(gulp.dest(function(file) {
        file.basename = file.basename.split('.')[0] + '.tpl';
        return './templates/';
    })
)
    .pipe(browserSync.reload({stream: true}));
});



// Таск для стилей
gulp.task('less', function () {
    return gulp.src(['./app//**/*.less', '!./app//**/_*.less'], { since: lastRun(less) })
    .pipe(sourcemaps.init())
    .pipe(less())
    .pipe(autoprefixer({cascade: false}))
    .pipe(concat('styleshet.css'))
    .pipe(csso())
    .pipe(sourcemaps.write('.'))
    .pipe(rename({ suffix: '.min' }))
    .pipe(gulp.dest('./static/static_files/styles'))
    .pipe(browserSync.reload({stream: true}));
});



// Сервер
gulp.task('browser-sync', function() { // Создаем таск browser-sync
    browserSync({ // Выполняем browser Sync
        //server: { // Определяем параметры сервера
        //    baseDir: 'templates' // Директория для сервера - app
        //},
        proxy: 'http://127.0.0.1:8000',
        notify: false, // Отключаем уведомления
        open: "external"
    });
});



// Наблюдаем за файлами
    gulp.task('watch', function() {
    gulp.watch('app/**/*.less', gulp.parallel('less')); // Наблюдение за less файлами
    gulp.watch('app/**/*.pug', gulp.parallel('pug')); // Наблюдение за less файлами
});
gulp.task('default', gulp.parallel('pug', 'less', 'browser-sync', 'watch'));