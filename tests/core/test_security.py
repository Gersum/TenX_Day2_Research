import pytest
import contextvars
from chimera_core.security import TenantContext, MissingTenantError

def test_tenant_context_set_get():
    """Verify strictly setting and getting the tenant ID in the current context."""
    with TenantContext("tenant-123"):
        assert TenantContext.get_current_tenant() == "tenant-123"

def test_tenant_context_missing():
    """Verify verification fails when no tenant context is active."""
    with pytest.raises(MissingTenantError):
        TenantContext.get_current_tenant()

def test_tenant_context_isolation():
    """Verify contexts are isolated and do not leak (ContextVars behavior)."""
    with TenantContext("tenant-outside"):
        assert TenantContext.get_current_tenant() == "tenant-outside"
        
        with TenantContext("tenant-inner"):
            assert TenantContext.get_current_tenant() == "tenant-inner"
        
        # Should return to outer context
        assert TenantContext.get_current_tenant() == "tenant-outside"
