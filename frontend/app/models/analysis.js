import DS from 'ember-data';
import Ember from 'ember';
//import {moment, ago} from 'ember-moment/computed';
//import moment from 'moment';
var inflector = Ember.Inflector.inflector;
inflector.irregular('analysis', 'analyses');

var Analysis = DS.Model.extend({
  dataset: DS.belongsTo('dataset', {async: true}),
  classifiers: DS.hasMany('classifier', {async: true}),
  title: DS.attr('string'),
  description: DS.attr('string'),
  classifier_ids: DS.attr(),
/*  hasHeader: DS.attr('boolean'),
  posLabel: DS.attr('number', {default: 1}),*/
  completed: DS.attr('boolean'),
/*  ignoreFirst: DS.attr('boolean'),
*/  test_outputs: DS.hasMany('test_outputs', {async: true}),
  created: DS.attr('date'),
/*  timeAgo: function() {
    return moment(this.get('date')).fromNow();
  }.property('created'),*/
  formattedDate: function() {
    return "Meh";
  }
});

export default Analysis;

