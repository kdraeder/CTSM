"""A JobLauncher for systems that use qsub"""

from ctsm_pylib.joblauncher.job_launcher_base import JobLauncherBase

class JobLauncherQsub(JobLauncherBase):

    def __init__(self, queue, walltime, account, required_args, extra_args):
        JobLauncherBase.__init__(self,
                                 queue=queue,
                                 walltime=walltime,
                                 account=account,
                                 required_args=required_args,
                                 extra_args=extra_args)

    def run_command(self, command, dry_run):
        # FIXME(wjs, 2018-08-25) Implement this
        pass
