class PipelineGen:
    def __init__(self, platform="github"): self.platform, self.stages = platform, []
    def add(self, name, cmds): self.stages.append({"name": name, "cmds": cmds})
    def generate(self):
        lines = ["name: CI", "on: [push]", "jobs:"]
        for s in self.stages:
            lines.append(f"  {s['name']}:
    runs-on: ubuntu-latest
    steps:")
            for c in s["cmds"]: lines.append(f"      - run: {c}")
        return "\n".join(lines)
