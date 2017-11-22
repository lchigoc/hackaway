# -*- coding: utf-8 -*-
import os
import tensorflow as tf

from config import FLAGS
from model import build_graph
from preprocess import train_data_iterator, test_data_helper


images, labels, keep_prob, loss, optimizer, accuracy = build_graph()
with tf.Session() as sess:
    saver = tf.train.Saver()
    sess.run(tf.global_variables_initializer())
    for step, (x_batch, y_batch) in enumerate(train_data_iterator()):
        _, loss_ = sess.run([optimizer, loss], feed_dict={images:x_batch,
                            labels:y_batch, keep_prob:0.5})
        print("Step {} -- Train loss {}".format(step, loss_))
        # eval stage
        if step % FLAGS.eval_steps == 0:
            x_batch_test, y_batch_test = test_data_helper()
            accuracy_ = sess.run(accuracy, feed_dict={images:x_batch_test, labels:y_batch_test, keep_prob:1.0})
            print("Step {} -- Test accuracy {}".format(step, accuracy_))
        # save stage
        if step % FLAGS.save_steps == 0 and step > FLAGS.min_save_steps:
            model_path = os.path.join(FLAGS.checkpoint_dir, FLAGS.model_name)
            saver.save(sess, model_path, global_step=step)
