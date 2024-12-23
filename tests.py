import pytest
import importlib
import sys
import io
import builtins

@pytest.mark.parametrize("original_sentence,encrypted_sentence",
                        [['python is fun!', 'udymts nx kzs!'],
                        ['aaa', 'fff'],
                        ['xyz', 'cde'],
                        ['A sentence with Capital letters.', 'F xjsyjshj bnym Hfunyfq qjyyjwx.'],
                        ['#$%^&*()', '#$%^&*()']
                        ])
def test_cipher(original_sentence, encrypted_sentence, monkeypatch):
    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        inputs = iter([original_sentence])
        m.setattr(builtins, "input", lambda _: next(inputs))
        m.setattr(sys, "stdout", mocked_stdout)
        sys.modules.pop("cipher", None)
        importlib.import_module(name="cipher", package="files")
    
    assert encrypted_sentence in mocked_stdout.getvalue().strip()