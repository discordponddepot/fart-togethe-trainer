from trainer.bootstrap import TrainerContext
from trainer.services.state_service import TrainerState
from trainer.services.cheat_service import CheatService


def make_ctx() -> TrainerContext:
    st = TrainerState(pid=None, attached=False)
    return TrainerContext(pid=None, dry_run=True, offsets={"fart_meter": 0, "fart_speed": 0, "ghost_flag": 0}, state=st)


def test_toggle_infinite_fart() -> None:
    ctx = make_ctx()
    svc = CheatService(ctx)
    assert svc.toggle_infinite_fart() is True
    assert ctx.state.infinite_fart is True
    assert svc.toggle_infinite_fart() is False


def test_toggle_fart_speed_multiplies() -> None:
    ctx = make_ctx()
    svc = CheatService(ctx)
    svc.toggle_fart_speed()
    assert ctx.state.fart_speed_mult == 3.0
    svc.toggle_fart_speed()
    assert ctx.state.fart_speed_mult == 1.0
</br>