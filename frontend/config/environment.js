/* jshint node: true */

module.exports = function(environment) {
  var ENV = {
    modulePrefix: 'frontend',
    environment: environment,
    baseURL: '/',
    locationType: 'auto',
    EmberENV: {
      FEATURES: {
        // Here you can enable experimental features on an ember canary build
        // e.g. 'with-controller': true
      }
    },

    APP: {
      // Here you can pass flags/options to your application instance
      // when it is created
      rootElement: "#ember-app"
    }
  };

  ENV.contentSecurityPolicy = {
  'default-src': "'none'",
  'script-src': "'self' https://cdn.mxpnl.com", // Allow scripts from https://cdn.mxpnl.com
  'font-src': "'self' http://fonts.gstatic.com", // Allow fonts to be loaded from http://fonts.gstatic.com
  'connect-src': "'self' https://api.mixpanel.com http://custom-api.local ws://0.0.0.0:35729 http://localhost:8000/", // Allow data (ajax/websocket) from api.mixpanel.com and custom-api.local
  'img-src': "'self'",
  'style-src': "'self' 'unsafe-inline' http://fonts.googleapis.com", // Allow inline styles and loaded CSS from http://fonts.googleapis.com
  'media-src': "'self'"
}

  if (environment === 'development') {
    // ENV.APP.LOG_RESOLVER = true;
    ENV.APP.LOG_ACTIVE_GENERATION = true;
    // ENV.APP.LOG_TRANSITIONS = true;
    // ENV.APP.LOG_TRANSITIONS_INTERNAL = true;
    ENV.APP.LOG_VIEW_LOOKUPS = true;
    ENV.APP.API_HOST = 'http://localhost:8000';
    ENV.APP.API_NAMESPACE = 'api';
  }

  if (environment === 'test') {
    // Testem prefers this...
    ENV.baseURL = '/';
    ENV.locationType = 'auto';

    // keep test console output quieter
    ENV.APP.LOG_ACTIVE_GENERATION = false;
    ENV.APP.LOG_VIEW_LOOKUPS = false;

    ENV.APP.rootElement = '#ember-testing';
  }

  if (environment === 'production') {

  }

  return ENV;
};
