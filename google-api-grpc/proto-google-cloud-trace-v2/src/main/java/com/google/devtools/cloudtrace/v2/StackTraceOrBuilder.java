// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: google/devtools/cloudtrace/v2/trace.proto

package com.google.devtools.cloudtrace.v2;

public interface StackTraceOrBuilder extends
    // @@protoc_insertion_point(interface_extends:google.devtools.cloudtrace.v2.StackTrace)
    com.google.protobuf.MessageOrBuilder {

  /**
   * <pre>
   * Stack frames in this stack trace. A maximum of 128 frames are allowed.
   * </pre>
   *
   * <code>.google.devtools.cloudtrace.v2.StackTrace.StackFrames stack_frames = 1;</code>
   */
  boolean hasStackFrames();
  /**
   * <pre>
   * Stack frames in this stack trace. A maximum of 128 frames are allowed.
   * </pre>
   *
   * <code>.google.devtools.cloudtrace.v2.StackTrace.StackFrames stack_frames = 1;</code>
   */
  com.google.devtools.cloudtrace.v2.StackTrace.StackFrames getStackFrames();
  /**
   * <pre>
   * Stack frames in this stack trace. A maximum of 128 frames are allowed.
   * </pre>
   *
   * <code>.google.devtools.cloudtrace.v2.StackTrace.StackFrames stack_frames = 1;</code>
   */
  com.google.devtools.cloudtrace.v2.StackTrace.StackFramesOrBuilder getStackFramesOrBuilder();

  /**
   * <pre>
   * The hash ID is used to conserve network bandwidth for duplicate
   * stack traces within a single trace.
   * Often multiple spans will have identical stack traces.
   * The first occurrence of a stack trace should contain both the
   * `stackFrame` content and a value in `stackTraceHashId`.
   * Subsequent spans within the same request can refer
   * to that stack trace by only setting `stackTraceHashId`.
   * </pre>
   *
   * <code>int64 stack_trace_hash_id = 2;</code>
   */
  long getStackTraceHashId();
}
