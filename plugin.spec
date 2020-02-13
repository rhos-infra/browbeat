config:
    plugin_type: test
subparsers:
    browbeat:
        description: The Browbeat performance test runner
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: Browbeat
              options:
                  install:
                    type: Bool
                    help: |
                      Runs the browbeat installer
                    default: False
                  config-file:
                      type: FileValue
                      help: |
                        The browbeat configuration to execute
                  monitor:
                      type: Bool
                      help: |
                        Setup collectd to monitor cloud
                      default: False
                  visualize:
                      type: Bool
                      help:
                        Visualize system metrics through grafana dashboards
                      default: False
                  containers:
                      type: Bool
                      help:
                        Use containers in monitor tasks
                      default: False
