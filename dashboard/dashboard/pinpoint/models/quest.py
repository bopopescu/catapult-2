# Copyright 2016 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel


class Quest(polymodel.PolyModel):
  """A description of work to do on a Change.

  Examples include building a binary or running a test. The concept is borrowed
  from Dungeon Main (go/dungeon-main). In Dungeon Main, Quests can depend
  on other Quests, but we're not that fancy here. All the Quests should run on a
  Change linearly (e.g. build, then test, then read test results). We'd like to
  replace this model with Dungeon Main entirely, when it's ready.
  """

  def Run(self, *args):
    raise NotImplementedError()


class FindIsolated(Quest):
  configuration = ndb.StringProperty(required=True)

  def Run(self):
    # TODO
    return (0,), ()


class RunTest(Quest):
  test_suite = ndb.StringProperty(required=True)
  test = ndb.StringProperty()

  def Run(self):
    # TODO
    return (0,), ()


class ReadTestResults(Quest):
  metric = ndb.StringProperty(required=True)

  def Run(self):
    # TODO
    return (0,), ()
