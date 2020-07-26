# coding: utf-8
#
# Copyright 2018 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for topic domain objects."""

from __future__ import absolute_import  # pylint: disable=import-only-modules
from __future__ import unicode_literals  # pylint: disable=import-only-modules

from core.domain import wipeout_domain
from core.tests import test_utils


class PendingDeletionRequestUnitTests(test_utils.GenericTestBase):
    """Tests for topic domain objects."""

    def setUp(self):
        super(PendingDeletionRequestUnitTests, self).setUp()
        self.signup('a@example.com', 'A')
        self.signup('b@example.com', 'B')
        self.user_id_a = self.get_user_id_from_email('a@example.com')

    def test_create_default_pending_deletion_request(self):
        """Tests the create_default_topic() function."""
        default_pending_deletion = (
            wipeout_domain.PendingDeletionRequest.create_default(
                self.user_id_a, 'a@example.com', [], []))
        self.assertEqual(default_pending_deletion.user_id, self.user_id_a)
        self.assertEqual(default_pending_deletion.email, 'a@example.com')
        self.assertEqual(default_pending_deletion.deletion_complete, False)
        self.assertEqual(default_pending_deletion.exploration_ids, [])
        self.assertEqual(default_pending_deletion.collection_ids, [])
        self.assertEqual(default_pending_deletion.activity_mappings, {})
