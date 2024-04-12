from typing import TYPE_CHECKING

from ...utils import (
    DIFFUSERS_SLOW_IMPORT,
    _LazyModule,
)


_import_structure = {"pipeline_ddpm": ["DDPMPipeline"]}
_import_structure.update({"custom_pipeline_ddpm": ["ConditionalDDPMPipeline"]}) # 추가


if TYPE_CHECKING or DIFFUSERS_SLOW_IMPORT:
    from .pipeline_ddpm import DDPMPipeline
    from .custom_pipeline_ddpm import ConditionalDDPMPipeline # 추가

else:
    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
    )
