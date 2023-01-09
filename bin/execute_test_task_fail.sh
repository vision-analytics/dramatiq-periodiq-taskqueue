python3 -c """from dramatiq_taskqueue import tasks; tasks.test_task_fail.send_with_options(
        args=('test_input',),
        on_failure=tasks.handle_task_failure,)"""