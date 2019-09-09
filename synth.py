# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This script is used to synthesize generated parts of this library."""

import synthtool as s
import synthtool.gcp as gcp
import synthtool.languages.java as java

gapic = gcp.GAPICGenerator()

service = 'trace'
versions = ['v1', 'v2']
config_pattern = '/google/devtools/cloudtrace/artman_cloudtrace_{version}.yaml'

# License header
license = """
/*
 * Copyright 2019 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
"""
protobuf_header = "// Generated by the protocol buffer compiler.  DO NOT EDIT!"
bad_license = """/\\*
 \\* Copyright 2018 Google LLC
 \\*
 \\* Licensed under the Apache License, Version 2.0 \\(the "License"\\); you may not use this file except
 \\* in compliance with the License. You may obtain a copy of the License at
 \\*
 \\* http://www.apache.org/licenses/LICENSE-2.0
 \\*
 \\* Unless required by applicable law or agreed to in writing, software distributed under the License
 \\* is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 \\* or implied. See the License for the specific language governing permissions and limitations under
 \\* the License.
 \\*/
"""

for version in versions:
    library = gapic.java_library(
        service=service,
        version=version,
        config_path=config_pattern.format(version=version),
        artman_output_name='',
        include_samples=True)

    s.replace(
        library / f'proto-google-cloud-{service}-{version}/src/**/*.java',
        protobuf_header,
        f"{license}{protobuf_header}"
    )
    s.replace(
        library / f'grpc-google-cloud-{service}-{version}/src/**/*.java',
        f"package com.google.devtools.cloudtrace.{version};",
        f"{license}package com.google.devtools.cloudtrace.{version};"
    )
    s.replace(
        library / f'proto-google-cloud-{service}-{version}/src/**/*Name.java',
        bad_license,
        license
    )

    s.copy(library / f'gapic-google-cloud-{service}-{version}/src', 'google-cloud-trace/src')
    s.copy(library / f'grpc-google-cloud-{service}-{version}/src', f'grpc-google-cloud-{service}-{version}/src')
    s.copy(library / f'proto-google-cloud-{service}-{version}/src', f'proto-google-cloud-{service}-{version}/src')
    s.copy(library / f'gapic-google-cloud-{service}-{version}/samples/src', 'samples/src')

    java.format_code(f'./grpc-google-cloud-{service}-{version}/src')
    java.format_code(f'./proto-google-cloud-{service}-{version}/src')

java.format_code('./google-cloud-trace/src')

common_templates = gcp.CommonTemplates()
templates = common_templates.java_library()
s.copy(templates, excludes=[
  '.gitignore',
  'README.md',
])

