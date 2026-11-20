from strictdoc.core.project_config import ProjectConfig


def create_config() -> ProjectConfig:
    return ProjectConfig(
        project_title="Fencing Vision Requirements",
        include_doc_paths=["*.sdoc", "*.sgra"],
        grammars={
            "@fencing-vision-requirement": "requirements.sgra",
        },
    )
